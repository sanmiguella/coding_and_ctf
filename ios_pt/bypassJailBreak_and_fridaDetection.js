// Bypass JB from:: https://codeshare.frida.re/@DevTraleski/ios-jailbreak-detection-bypass-palera1n/
const jailbreakPaths = [
            "/var/mobile/Library/Preferences/ABPattern", // A-Bypass
            "/usr/lib/ABDYLD.dylib", // A-Bypass,
            "/usr/lib/ABSubLoader.dylib", // A-Bypass
            "/usr/sbin/frida-server", // frida
            "/etc/apt/sources.list.d/electra.list", // electra
            "/etc/apt/sources.list.d/sileo.sources", // electra
            "/.bootstrapped_electra", // electra
            "/usr/lib/libjailbreak.dylib", // electra
            "/jb/lzma", // electra
            "/.cydia_no_stash", // unc0ver
            "/.installed_unc0ver", // unc0ver
            "/jb/offsets.plist", // unc0ver
            "/usr/share/jailbreak/injectme.plist", // unc0ver
            "/etc/apt/undecimus/undecimus.list", // unc0ver
            "/var/lib/dpkg/info/mobilesubstrate.md5sums", // unc0ver
            "/Library/MobileSubstrate/MobileSubstrate.dylib",
            "/jb/jailbreakd.plist", // unc0ver
            "/jb/amfid_payload.dylib", // unc0ver
            "/jb/libjailbreak.dylib", // unc0ver
            "/usr/libexec/cydia/firmware.sh",
            "/var/lib/cydia",
            "/etc/apt",
            "/private/var/lib/apt",
            "/private/var/Users/",
            "/var/log/apt",
            "/Applications/Cydia.app",
            "/private/var/stash",
            "/private/var/lib/apt/",
            "/private/var/lib/cydia",
            "/private/var/cache/apt/",
            "/private/var/log/syslog",
            "/private/var/tmp/cydia.log",
            "/Applications/Icy.app",
            "/Applications/MxTube.app",
            "/Applications/RockApp.app",
            "/Applications/blackra1n.app",
            "/Applications/SBSettings.app",
            "/Applications/FakeCarrier.app",
            "/Applications/WinterBoard.app",
            "/Applications/IntelliScreen.app",
            "/private/var/mobile/Library/SBSettings/Themes",
            "/Library/MobileSubstrate/CydiaSubstrate.dylib",
            "/System/Library/LaunchDaemons/com.ikey.bbot.plist",
            "/Library/MobileSubstrate/DynamicLibraries/Veency.plist",
            "/Library/MobileSubstrate/DynamicLibraries/LiveClock.plist",
            "/System/Library/LaunchDaemons/com.saurik.Cydia.Startup.plist",
            "/Applications/Sileo.app",
            "/var/binpack",
            "/Library/PreferenceBundles/LibertyPref.bundle",
            "/Library/PreferenceBundles/ShadowPreferences.bundle",
            "/Library/PreferenceBundles/ABypassPrefs.bundle",
            "/Library/PreferenceBundles/FlyJBPrefs.bundle",
            "/Library/PreferenceBundles/Cephei.bundle",
            "/Library/PreferenceBundles/SubstitutePrefs.bundle",
            "/Library/PreferenceBundles/libhbangprefs.bundle",
            "/usr/lib/libhooker.dylib",
            "/usr/lib/libsubstitute.dylib",
            "/usr/lib/substrate",
            "/usr/lib/TweakInject",
            "/var/binpack/Applications/loader.app", // checkra1n
            "/Applications/FlyJB.app", // Fly JB X
            "/Applications/Zebra.app", // Zebra
            "/Library/BawAppie/ABypass", // ABypass
            "/Library/MobileSubstrate/DynamicLibraries/SSLKillSwitch2.plist", // SSL Killswitch
            "/Library/MobileSubstrate/DynamicLibraries/PreferenceLoader.plist", // PreferenceLoader
            "/Library/MobileSubstrate/DynamicLibraries/PreferenceLoader.dylib", // PreferenceLoader
            "/Library/MobileSubstrate/DynamicLibraries", // DynamicLibraries directory in general
            "/var/mobile/Library/Preferences/me.jjolano.shadow.plist",
            "/bin/bash",
            "/usr/sbin/sshd",
];

//App URL list in lower case for canOpenURL
const canOpenURL = [
    "cydia",
    "activator",
    "filza",
    "sileo",
    "undecimus",
    "zbra"
]

if (ObjC.available) {
    try {
        //Hooking fileExistsAtPath:
        Interceptor.attach(ObjC.classes.NSFileManager["- fileExistsAtPath:"].implementation, {
            onEnter(args) {
                // Use a marker to check onExit if we need to manipulate
                // the response.
                this.is_common_path = false;

                // Extract the path
                this.path = new ObjC.Object(args[2]).toString();

                // check if the looked up path is in the list of common_paths
                if (jailbreakPaths.indexOf(this.path) >= 0) {
                    // Mark this path as one that should have its response
                    // modified if needed.
                    this.is_common_path = true;
                }
            },

            onLeave(retval) {
                // stop if we dont care about the path
                if (!this.is_common_path) {
                    return;
                }

                // ignore failed lookups
                if (retval.isNull()) {
                    return;
                }
                console.log(`fileExistsAtPath: bypassing ` + this.path);
                retval.replace(new NativePointer(0x00));
            },
        });

        //Hooking fopen
        Interceptor.attach(Module.findExportByName(null, "fopen"), {
            onEnter(args) {
                this.is_common_path = false;

                // Extract the path
                this.path = args[0].readCString();
                
		// check if the looked up path is in the list of common_paths
                if (jailbreakPaths.indexOf(this.path) >= 0) {
                    // Mark this path as one that should have its response
                    // modified if needed.
                    this.is_common_path = true;
                }
            },

            onLeave(retval) {
                // stop if we dont care about the path
                if (!this.is_common_path) {
                    return;
                }

                // ignore failed lookups
                if (retval.isNull()) {
                    return;
                }

                console.log(`fopen: bypassing` + this.path);
                retval.replace(new NativePointer(0x00));
            },
        });

        //Hooking canOpenURL for Cydia
        Interceptor.attach(ObjC.classes.UIApplication["- canOpenURL:"].implementation, {
            onEnter(args) {
                this.is_flagged = false;
                
			// Extract the path
                this.path = new ObjC.Object(args[2]).toString();
                let app = this.path.split(":")[0].toLowerCase();
                
		if (canOpenURL.indexOf(app) >= 0) {
                    this.is_flagged = true;
                }
            },

            onLeave(retval) {
                if (!this.is_flagged) {
                    return;
                }

                // ignore failed
                if (retval.isNull()) {
                    return;
                }
                
		console.log(`canOpenURL: ` +
                    this.path + ` was successful with: ` +
                    retval.toString() + `, bypassing.`);
                
		retval.replace(new NativePointer(0x00));
            }
        });

        //Hooking libSystemBFork
        const libSystemBdylibFork = Module.findExportByName("libSystem.B.dylib", "fork");
        
	   if (libSystemBdylibFork) {
            Interceptor.attach(libSystemBdylibFork, {
                onLeave(retval) {
                    // already failed forks are ok
                    if (retval.isNull()) {
                        return;
                    }
        
	            console.log(`Call to libSystem.B.dylib::fork() was successful with ` +
                        retval.toString() + ` marking it as failed.`);
                    retval.replace(new NativePointer(0x0));
                },
            });
        }
        
        //Hooking libSystemBdylib stat64
        const libSystemBdylibStat64 = Module.findExportByName("libSystem.B.dylib", "stat64");

        if (libSystemBdylibStat64) {
            Interceptor.attach(libSystemBdylibStat64, {
                onEnter: function(args) {
                    this.is_common_path = true;
                    this.arg = Memory.readUtf8String(args[0]);

                    for (var path in jailbreakPaths) {
                        if (this.arg.indexOf(jailbreakPaths[path]) > -1) {
                            this.is_common_path = false;
                            //return -1;
                        }
                    }
                },

                onLeave: function(retval) {
                    if(retval.isNull()){
                        return;
                    }
                    
                    if (!this.is_common_path) {
                        console.log(`stat64: bypass` + this.arg);
                        retval.replace(-1);
                    }
                }
            });
        }
        
        //Hooking libSystemBdylib stat
        const libSystemBdylibStat = Module.findExportByName("libSystem.B.dylib", "stat");

        if (libSystemBdylibStat) {
            Interceptor.attach(libSystemBdylibStat, {
                onEnter: function(args) {
                    this.is_common_path = true;
                    this.arg = Memory.readUtf8String(args[0]);
                    for (var path in jailbreakPaths) {
                        if (this.arg.indexOf(jailbreakPaths[path]) > -1) {
                            this.is_common_path = false;
                            //return -1;
                        }
                    }
                },
                onLeave: function(retval) {
                    if(retval.isNull()){
                        return;
                    }
                    
                    if (!this.is_common_path) {
                        console.log(`stat: bypass` + this.arg);
                        retval.replace(-1);
                    }
                }
            });
        }
        
    } catch (err) {
        console.log("Exception : " + err.message);
    }
} else {
    console.log("Objective-C Runtime is not available!");
}


// TYSM chatgpt for giving me the skeleton code.
const hookSwiftFunction = function() {
    var address = Module.findExportByName("INSERT_APP_NAME_HERE","$s16IOSSecuritySuiteAAC20amIReverseEngineeredSbyFZ");
    var amIReverseEngineered = new NativeFunction(address, 'bool', []);

    Interceptor.replace(amIReverseEngineered, new NativeCallback(function() {
        console.log('\n[*] Hooked $s16IOSSecuritySuiteAAC20amIReverseEngineeredSbyFZ');
        console.log('[*] Bypassing frida detection now.');
        return 0; // Return False.
    }, 'bool', []));
};

hookSwiftFunction();