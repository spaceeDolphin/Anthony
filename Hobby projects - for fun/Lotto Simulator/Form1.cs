using System.Data;

namespace Lotto_Simulator
{
    public partial class Form1 : Form
    {
        Random random;
        public Form1()
        {
            InitializeComponent();
            random = new Random();

            
        }

        int[] rowCurrent = new int[7];

        void ColorRowView(int textBoxNumber, Color color)
        {
            switch (textBoxNumber)
            {
                case 1:
                    txt1.BackColor = color;
                    break;
                case 2:
                    txt2.BackColor = color;
                    break;
                case 3:
                    txt3.BackColor = color;
                    break;
                case 4:
                    txt4.BackColor = color;
                    break;
                case 5:
                    txt5.BackColor = color;
                    break;
                case 6:
                    txt6.BackColor = color;
                    break;
                case 7:
                    txt7.BackColor = color;
                    break;
                case 8:
                    txt8.BackColor = color;
                    break;
                case 9:
                    txt9.BackColor = color;
                    break;
                case 10:
                    txt10.BackColor = color;
                    break;
                case 11:
                    txt11.BackColor = color;
                    break;
                case 12:
                    txt12.BackColor = color;
                    break;
                case 13:
                    txt13.BackColor = color;
                    break;
                case 14:
                    txt14.BackColor = color;
                    break;
                case 15:
                    txt15.BackColor = color;
                    break;
                case 16:
                    txt16.BackColor = color;
                    break;
                case 17:
                    txt17.BackColor = color;
                    break;
                case 18:
                    txt18.BackColor = color;
                    break;
                case 19:
                    txt19.BackColor = color;
                    break;
                case 20:
                    txt20.BackColor = color;
                    break;
                case 21:
                    txt21.BackColor = color;
                    break;
                case 22:
                    txt23.BackColor = color;
                    break;
                case 23:
                    txt23.BackColor = color;
                    break;
                case 24:
                    txt24.BackColor = color;
                    break;
                case 25:
                    txt25.BackColor = color;
                    break;
                case 26:
                    txt26.BackColor = color;
                    break;
                case 27:
                    txt27.BackColor = color;
                    break;
                case 28:
                    txt28.BackColor = color;
                    break;
                case 29:
                    txt29.BackColor = color;
                    break;
                case 30:
                    txt30.BackColor = color;
                    break;
                case 31:
                    txt31.BackColor = color;
                    break;
                case 32:
                    txt32.BackColor = color;
                    break;
                case 33:
                    txt33.BackColor = color;
                    break;
                case 34:
                    txt34.BackColor = color;
                    break;
            }
        }

        void ClearRowView()
        {
            for (int i = 0; i < 35; i++)
            {
                ColorRowView(i, Color.White);
            }
        }

        void RandomRow(out int[] randomRow, bool rowView = true)
        {
            if (rowView)
            {
                ClearRowView();
            }
            randomRow = new int[7];
            int[] sampleSpace = new int[] {1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34};
            for (int i = 0; i < 7; i++)
            {
                int x = random.Next(1, sampleSpace.Length);
                randomRow[i] = sampleSpace[x];
                if (rowView)
                {
                    ColorRowView(sampleSpace[x], Color.Red);
                }
                sampleSpace = sampleSpace.Where(e => e != sampleSpace[x]).ToArray();
            }
        }

        string RowText(int[] row)
        {
            string rowText = "";
            for (int i = 0; i < row.Length; i++)
            {
                rowText += row[i].ToString() + " ";
            }
            return rowText;
        }

        int CorrectNumbers(int[] row, int[] rowTry)
        {
            int correct = 0;
            foreach (int x in row)
            {
                foreach (int y in rowTry)
                {
                    if (x == y)
                    {
                        correct += 1;
                    }
                }
            }
            return correct;
        }

        void ClearProgram()
        {
            txtSimResult2.Clear();
            txtSimResult3.Clear();
            txtSimResult4.Clear();
            txtSimResult5.Clear();
            txtSimResult6.Clear();
            txtSimResult7.Clear();
            progressBarSim.Value = 0;
        }

        private void btnRow_Click(object sender, EventArgs e)
        {
            RandomRow(out int[] row);
            txtRow.Text = RowText(row);
            rowCurrent = row;
            btnPlay.Enabled = true;
        }

        private void btnPlay_Click(object sender, EventArgs e)
        {
            int result;
            RandomRow(out int[] rowLotto, false);
            result = CorrectNumbers(rowLotto, rowCurrent);
            txtLotto.Text = RowText(rowLotto);
            txtResult.Text = result.ToString() + " riktige!";
            txtRowsPlayed.AppendText(RowText(rowCurrent) + Environment.NewLine);
        }

        private void btnWin_Click(object sender, EventArgs e)
        {
            ClearProgram();
            int win = 0, result = 0, tries = 0;
            if (rdo4.Checked) { win = 4; }
            if (rdo5.Checked) { win = 5; }
            if (rdo6.Checked) { win = 6; }
            if (rdo7.Checked) { win = 7; }

            //Initialize Lotto Numbers
            RandomRow(out int[] rowLotto, false);
            txtLotto.Text = RowText(rowLotto);

            while (result < win)
            {
                string rowText;
                //Generating Row
                RandomRow(out int[] rowTry);
                rowText = RowText(rowTry);
                txtRow.Text = rowText;
                txtRowsPlayed.AppendText(rowText + Environment.NewLine);

                //Checking Result
                result = CorrectNumbers(rowLotto, rowTry);
                txtResult.Text = result.ToString() + " riktige!";

                tries++;
                numTries.Value = tries;
                Application.DoEvents();
                Thread.Sleep(20);
            }
        }

        private void btnMultipleTries_Click(object sender, EventArgs e)
        {
            //Initialize Lotto Numbers
            RandomRow(out int[] rowLotto, false);
            txtLotto.Text = RowText(rowLotto);

            int tries = Convert.ToInt32(numTries.Value);
            int two = 0; int three = 0; int four = 0; int five = 0; int six = 0; int seven = 0;
            txtSimResult2.Text = two.ToString();
            txtSimResult3.Text = three.ToString();
            txtSimResult4.Text = four.ToString();
            txtSimResult5.Text = five.ToString();
            txtSimResult6.Text = six.ToString();
            txtSimResult7.Text = seven.ToString();
            progressBarSim.Maximum = tries;

            for (int i = 0; i < tries; i++)
            {
                string rowText; int result;
                //Generating Row
                RandomRow(out int[] rowTry);
                rowText = RowText(rowTry);
                txtRow.Text = rowText;
                txtRowsPlayed.AppendText(rowText + Environment.NewLine);

                //Checking Result
                result = CorrectNumbers(rowLotto, rowTry);
                txtResult.Text = result.ToString() + " riktige!";
                switch(result)
                {
                    case 2:
                        two++;
                        txtSimResult2.Text = two.ToString();
                        break;
                    case 3:
                        three++;
                        txtSimResult3.Text = three.ToString();
                        break;
                    case 4:
                        four++;
                        txtSimResult4.Text = four.ToString();
                        break;
                    case 5:
                        five++;
                        txtSimResult5.Text = five.ToString();
                        break;
                    case 6:
                        six++;
                        txtSimResult6.Text = six.ToString();
                        break;
                    case 7:
                        seven++;
                        txtSimResult7.Text = seven.ToString();
                        break;
                    default:
                        break;
                }
                progressBarSim.Value = i+1;
                Application.DoEvents();
                Thread.Sleep(20);
            }
            
        }
    }
}