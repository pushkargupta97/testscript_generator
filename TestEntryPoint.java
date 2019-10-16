
import com.relevantcodes.extentreports.ExtentReports;
import com.relevantcodes.extentreports.ExtentTest;
import com.relevantcodes.extentreports.LogStatus;

import py4j.GatewayServer;

public class TestEntryPoint {
	
	private ExtentTest test;
	private ExtentReports report;
	
	public TestEntryPoint() {
		report = new ExtentReports(System.getProperty("user.dir") + "\\ExtentResults.html");
		test = report.startTest("ExtentDemo");
	}
	
//	public LogStatus getPass() {
//		return LogStatus.PASS ;
//	}
//	public LogStatus getFail() {
//		return LogStatus.FAIL ;
//	}
	
	public void reportPass(String usermsg) {
		test.log(LogStatus.PASS, usermsg);
	}
	
	public void reportFail(String usermsg) {
		test.log(LogStatus.FAIL, usermsg);
	}
	
	public ExtentTest getTest() {
		return test ;
	}
	
	public ExtentReports getReport() {
		return report ;
	}
	
	public void endAll() {
		report.endTest(test);
		report.flush();
	}
	
	public static void main(String[] args) {
		GatewayServer gatewayServer = new GatewayServer(new TestEntryPoint(),25537);
		gatewayServer.start();
		System.out.println("Gateway Server Started");
	}
}

