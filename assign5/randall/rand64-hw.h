#ifndef RAND64_HW
#define RAND64_HW

#include <stdbool.h>
#include <cpuid.h>


/* Description of the current CPU.  */
struct cpuid { unsigned eax, ebx, ecx, edx; };

/* Return information about the CPU.  See <http://wiki.osdev.org/CPUID>.  */
struct cpuid
cpuid (unsigned int leaf, unsigned int subleaf);


/* Return true if the CPU supports the RDRAND instruction.  */
_Bool
rdrand_supported (void);

/* Initialize the hardware rand64 implementation.  */
void
hardware_rand64_init (void);

/* Return a random value, using hardware operations.  */
unsigned long long
hardware_rand64 (void);

/* Finalize the hardware rand64 implementation.  */
void
hardware_rand64_fini (void);


#endif
