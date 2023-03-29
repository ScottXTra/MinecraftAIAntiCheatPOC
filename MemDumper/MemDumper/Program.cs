using System;
using System.IO;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Threading.Tasks;

class Program
{
    static void Main(string[] args)
    {
        // Define the memory addresses to read
        long[] addresses = { 0x2D6D3FEC98 };

        // Open the process to read memory from
        Process process = Process.GetProcessesByName("Minecraft.Windows")[0];

        String file = "test_values.csv";
        //String file = "train_values.csv";

        using (StreamWriter writer = new StreamWriter(file))
        {

           // writer.WriteLine("pos_x,pos_y,pos_z,velocity_x,velocity_y,velocity_z,flying");
            writer.WriteLine("pos_x,pos_y,pos_z,velocity_x,velocity_y,velocity_z");
        }

        // Start a loop to continuously read memory values and write them to the CSV file when the "f" key is pressed
        long yposaddr = 0x177280B6C70;
        long yveladdr = 0x177280B6C7C;
        long flyingval = 0x177236DC16C;
        long onground = 0x17727344050;
        int sleepTime = 20;
        DateTime nextWriteTime = DateTime.UtcNow.AddMilliseconds(sleepTime);
        while (true)
        {

            if (DateTime.UtcNow >= nextWriteTime)
            {
                using (StreamWriter writer = new StreamWriter(file, true))
                {
                    // Read the values at the specified addresses and write them to the CSV file
                    float XPOS = ReadMemory(process.Handle, (IntPtr)yposaddr - 4);
                    float YPOS = ReadMemory(process.Handle, (IntPtr)yposaddr);
                    float ZPOS = ReadMemory(process.Handle, (IntPtr)yposaddr + 4);
                    float XVEL = ReadMemory(process.Handle, (IntPtr)yveladdr - 4);
                    float YVEL = ReadMemory(process.Handle, (IntPtr)yveladdr);
                    float ZVEL = ReadMemory(process.Handle, (IntPtr)yveladdr + 4);
                    int Flyingval = ReadMemoryInt(process.Handle, (IntPtr)flyingval);
                    int onGround = ReadMemoryInt(process.Handle, (IntPtr)onground);
                    // int shiftKeyDown = Convert.ToInt32((GetAsyncKeyState(0x10) & 0x8000) != 0);
                   // writer.WriteLine("{0},{1},{2},{3},{4},{5},{6}", XPOS, YPOS, ZPOS, XVEL, YVEL, ZVEL, Flyingval);
                   // Console.WriteLine("{0},{1},{2},{3},{4},{5},{6}", XPOS, YPOS, ZPOS, XVEL, YVEL, ZVEL, Flyingval);
                   writer.WriteLine("{0},{1},{2},{3},{4},{5}", XPOS, YPOS, ZPOS, XVEL, YVEL, ZVEL);
                    Console.WriteLine("{0},{1},{2},{3},{4},{5}", XPOS, YPOS, ZPOS, XVEL, YVEL, ZVEL);

                }
                nextWriteTime = nextWriteTime.AddMilliseconds(sleepTime);
            }
            Task.Delay(1).Wait();
        }
    }

    // Read a 32-bit float from the specified memory address
    static float ReadMemory(IntPtr handle, IntPtr address)
    {
        byte[] buffer = new byte[4];
        ReadProcessMemory(handle, address, buffer, buffer.Length, out int bytesRead);
        return BitConverter.ToSingle(buffer, 0);
    }
    static int ReadMemoryInt(IntPtr handle, IntPtr address)
    {
        byte[] buffer = new byte[4];
        ReadProcessMemory(handle, address, buffer, buffer.Length, out int bytesRead);
        return BitConverter.ToInt32(buffer, 0);
    }
    // Windows API functions for reading process memory and keyboard state
    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool ReadProcessMemory(
        IntPtr hProcess,
        IntPtr lpBaseAddress,
        [Out] byte[] lpBuffer,
        int dwSize,
        out int lpNumberOfBytesRead
    );

    [DllImport("user32.dll")]
    public static extern short GetAsyncKeyState(int vKey);
}
