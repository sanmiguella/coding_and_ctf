using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime thisYear = new DateTime(2020, 3, 27);

            bool isLeapYear = DateTime.IsLeapYear(thisYear.Year);

            DateTime thisMoment = DateTime.Now;
            TimeSpan time = thisMoment.TimeOfDay;

            DateTime date = DateTime.Today;

            Console.WriteLine("Full date : " + date);
            Console.WriteLine("Full time : " + time);

            Console.WriteLine("\nYear :\t" + thisYear.Year);
            Console.WriteLine("Date :\t" + thisMoment.Day);
            Console.WriteLine("Day  :\t" + thisMoment.DayOfWeek);

            Console.WriteLine("\nHour : " + thisMoment.Hour);
            Console.WriteLine("Minute : " + thisMoment.Minute);
            Console.WriteLine("Second : " + thisMoment.Second);

            Console.WriteLine("\nIs leap year ? " + isLeapYear);

            // Wait for user to acknowledge the results.
            Console.WriteLine("\nPress enter to terminate..");
            Console.Read();
        }
    }
}
