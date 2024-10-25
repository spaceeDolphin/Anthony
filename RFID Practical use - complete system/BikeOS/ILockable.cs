using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BikeOS
{
    public interface ILockable
    {
        int StationId { get; set; }
        string TagId { get; set; }
        void RegisterLock();
        void RegisterUnlock();
    }
}