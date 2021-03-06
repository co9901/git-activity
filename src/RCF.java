import java.util.ArrayList;

public class RCF extends Metric {
	
	public RCF(Target target) {
		super(target);
	}

	private double getMedianCommitinterval(int timeStart, int timeEnd) {
		int timeLast = -1;
		ArrayList<Double> interval = new ArrayList<Double>();
		for (Integer time : this.target.getListCommitTime()) {
			if (timeStart <= time && time <= timeEnd) {
				if (timeLast >= 0)
					interval.add((double)Math.abs(timeLast - time));
				timeLast = time;
			}
		}
		return getMedian(interval);
	}

	public double getValue(int timeEnd) {
		double mcia = getMedianCommitinterval(timeEnd - 24 * DEFAULT_INTERVAL, timeEnd);
		double mci6 = getMedianCommitinterval(timeEnd - DEFAULT_INTERVAL, timeEnd);
		double ratio = mcia / (mci6 + 1E-9);
		double rcf = 100. / (1 + Math.exp(-ratio));
		return (rcf - 50.0) * 2.0;
	}
}
