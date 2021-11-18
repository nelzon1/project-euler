using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Euler29
{
    class Program
    {
        static void Main(string[] args)
        {
            long powa;
            List<long> powers = new List<long>();
            for (long a=2;a<=100;a++)
            {
                for (long b=2;b<=100;b++)
                {
                    powa = (long)Math.Pow(a, b);
                    if (!powers.Contains(powa))
                        powers.Add(powa);

                }
            }

            Console.WriteLine(powers.Count);
            //long[] answers = powers.ToArray();
            //powers.ForEach(i => Console.WriteLine(i.ToString()));
        }
    }
}
