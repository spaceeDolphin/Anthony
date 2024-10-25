using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;

namespace BikeOS
{
    public class Bike:Vehicle
    {
        public override int Id { get; set; }
        public override string Name { get; set; }
        public string Color { get; set; }
        public Bike(int id) : base(id) { Name = "Bike"; Color = "Yellow"; }
        public override string ToString()
        {
            return "This is a bike";
        }
    }
}