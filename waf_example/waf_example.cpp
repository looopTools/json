#include <nlohmann/json.hpp>

#include <string>

#include <iostream>

int main(void)
{
    nlohmann::json obj;
    obj["key"] = "value";

    std::cout << obj["key"].get<std::string>() << std::endl;
    return 0;
}
