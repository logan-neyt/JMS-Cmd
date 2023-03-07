package xyz.teklen.jmscmd.arguments;

public class InvalidArgumentException extends RuntimeException {
    public InvalidArgumentException() {
        super();
    }

    public InvalidArgumentException(String msg) {
        super(msg);
    }

    public InvalidArgumentException(String msg, Throwable cause) {
        super(msg, cause);
    }

    public InvalidArgumentException(Throwable cause) {
        super(cause);
    }
}
