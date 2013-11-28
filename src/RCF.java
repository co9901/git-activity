
import java.util.ArrayList;


public class RCF extends Metric {
    
    public RCF(Target target) {
        super(target);
    }

    private double getMedianCommitInterval(int timeStart, int timeEnd) {
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

    public double getValue(int timeEnd, int interval) {
        double mcia = getMedianCommitInterval(timeEnd - 120*MONTH, timeEnd);
        double mci6 = getMedianCommitInterval(timeEnd - interval*MONTH, timeEnd);
        double ratio = mcia / (mci6 + 1E-9);
        double rcf = 100. * (1 - 1 / (1 + Math.pow(ratio, 2)));
        return rcf;
    }
}
