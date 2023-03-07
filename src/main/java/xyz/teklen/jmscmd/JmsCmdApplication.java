package xyz.teklen.jmscmd;

import java.util.Properties;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import lombok.extern.slf4j.Slf4j;

@SpringBootApplication
@Slf4j
public class JmsCmdApplication implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(JmsCmdApplication.class, args);
	}

	@Override
	public void run(String... argz) {
		log.debug("Run...");	// TODO remove

		// TODO Parse args

		// TODO If help, print help and exit.

		// TODO Get task

		// TODO Get connection details

		// TODO Create connction (listening / sending)

		// TODO Perform task
	}
}
