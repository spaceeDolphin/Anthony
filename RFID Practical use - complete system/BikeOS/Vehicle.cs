using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BikeOS
{
    public abstract class Vehicle
    {
        public abstract string Name { get; set; }
        public abstract int Id { get; set; }
        public override string ToString()
        {
            return "This is a vehicle";
        }
        public Vehicle(int id)
        {
            Id = id;
        }
    }
}