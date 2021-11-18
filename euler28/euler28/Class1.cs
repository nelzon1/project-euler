using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Class1
    {
        static void Main(string[] args)
        {
        int n = 1001;
            int[,] grid = new int[n,n];
        squareFill(grid);
        int sum = 0;
        for (int y = 0;y<n;y++)
        {
            for (int x = 0; x < n; x++ )
            {
                //Console.Write(grid[n-y-1, x]);
                //if (x == n - 1) Console.Write('\n');
               // else Console.Write('\t');
                if (x == y || x + y == n)
                    sum += grid[y, x];
            }

          
        }
        Console.WriteLine(grid.Length);
        Console.WriteLine(sum);
        Console.Read();

    }

        public static void squareFill(int[,] square)
        {
            //up = 0, right = 1, down = 2, left = 3
            int direction = 0;
            int x = (int)(Math.Sqrt(square.Length) / 2);
            int y = x;
            bool notFinished = true;
            int count = 1, position=0, line = 0;
            while (notFinished)
            {
                square[y,x] = count;
                //check for finished
                if (y == (int) (Math.Sqrt(square.Length )- 1) && x == y)
                    break;

                //check for end of line and change direction if needed
                if (position == line)
                {
                    if (direction % 2 == 0)
                    {
                        line++;
                    }
                    direction++;
                    position = 0;
                }
                //increment
                switch (direction % 4)
                {
                    case 0:
                        y++;
                        break;
                    case 1:
                        x++;
                        break;
                    case 2:
                        y--;
                        break;
                    case 3:
                        x--;
                        break;
                }
                position++;
                count++;
            }
        }

    }

