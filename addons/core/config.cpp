class CfgPatches {
    class InteceptPython_Core {
        name = "Intercept Python - Core";
        units[] = {};
        weapons[] = {};
        requiredVersion = 1.70;
        requiredAddons[] = {"Intercept_Core"};
        author = "Intercept Python Team";
        authors[] = {"Zakant","Overfl0"};
        url = "https://github.com/intercept/intercept-python";
    };
};

class Intercept {
    class InterceptPython {
        class InterceptPython_Core {
            pluginName = "InterceptPython";
        };
    };
};
