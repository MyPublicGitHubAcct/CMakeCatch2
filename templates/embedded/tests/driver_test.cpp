#include <catch2/catch.hpp>
extern "C" {
#include "../drivers/driver.h"
}

Test(suitename, testname)
{
    int val = driver();
    cr_expect(val == 7, "driver() should return 6");
}
