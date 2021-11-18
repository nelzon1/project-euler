using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace euler31
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0, penny = 1, two = 2, nickel = 5, dime = 10, twenty = 20, half = 50, dollar =100, toonie=200;

            for (int p=0;p<=200;p++)
            {
                for (int too = 0; too <= 100; too++)
                {
                    for (int n = 0; n <= 40; n++)
                    {
                        for (int d = 0; d <= 20; d++)
                        {
                            for (int t = 0; t <= 10; t++)
                            {
                                for (int h = 0; h <= 4; h++)
                                {
                                    for (int dol = 0; dol <= 2; dol++)
                                    {
                                        for (int to = 0; to <= 1; to++)
                                        {
                                            if (penny * p + two * too + nickel * n + dime * d + twenty * t + half * h + dollar *dol +toonie * to == 200)
                                                count += 1;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            Console.WriteLine(count);
        }
    }
}
