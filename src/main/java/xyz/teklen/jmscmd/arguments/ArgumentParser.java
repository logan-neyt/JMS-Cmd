package xyz.teklen.jmscmd.arguments;

import java.util.LinkedList;
import java.util.List;
import java.util.Properties;

public class ArgumentParser {
    public Properties parse(String[] rawArgs) {
		Properties argPairs = new Properties();
        List<String> positionalArgs = new LinkedList<>();
		String key = null;
		for (String argument : rawArgs) {
			if (key != null) {
				if (argument.startsWith("-")) { // E.g: -a -b
					argPairs.put(key, "true");
					key = null;
				} else {
					argPairs.put(key, argument);
					key = null;
                    continue;
				}
			}

            if (argument.startsWith("-")) {
                if (argument.length() == 1) // E.g: -
                    throw new InvalidArgumentException("Invalid argument \"" + argument + "\"");
                
                if (argument.startsWith("--")) {    // Long argument, E.g: --help
                    if (argument.contains("=")) {   // E.g: --key=value
                        var argumentParts = argument.split("=");
                        argPairs.put(argumentParts[0].substring(2), argument.substring(argumentParts[0].length()));
                    } else {
                        key = argument.substring(2);
                    }

                } else {
                    if (argument.length() > 2) {    // E.g: -abcd
                        for (int i = 1; i < argument.length() - 1; i++) {
                            argPairs.put(Character.toString(argument.charAt(i)), "true");
                        }
                        key = Character.toString(argument.charAt(argument.length() - 1));
                    }
                }

            } else {    // Positional argument, E.g: posArg1 posArg2
                positionalArgs.add(argument);
            }
		}

        if (key != null) {  // If last argument is a flag
            argPairs.put(key, "true");
        }

        return argPairs;  // TODO Return argPairs and positionalArgs
	}
}
