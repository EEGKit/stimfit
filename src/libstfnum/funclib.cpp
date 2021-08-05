// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

#include <cfloat>
#include <cmath>
#include <sstream>

#include "./fit.h"
#include "./measure.h"
#include "./funclib.h"

std::vector< stfnum::storedFunc > stfnum::GetFuncLib() {
    std::vector< stfnum::storedFunc > funcList;
    
    // Monoexponential function, free fit:
    std::vector<stfnum::parInfo> parInfoMExp=getParInfoExp(1);
    funcList.push_back(stfnum::storedFunc("Monoexponential",parInfoMExp,fexp,fexp_init,fexp_jac,true));

    // Monoexponential function, offset fixed to baseline:
    parInfoMExp[2].toFit=false;
    funcList.push_back(stfnum::storedFunc("Monoexponential, offset fixed to baseline",
                                         parInfoMExp,fexp,fexp_init,fexp_jac,true));

    // Monoexponential function, starting with a delay, start fixed to baseline:
    std::vector<stfnum::parInfo> parInfoMExpDe(4);
    parInfoMExpDe[0].toFit=false; parInfoMExpDe[0].desc="Baseline"; parInfoMExpDe[0].scale=stfnum::yscaleoffset; parInfoMExpDe[0].unscale=stfnum::yunscaleoffset; 
    parInfoMExpDe[1].toFit=true; parInfoMExpDe[1].desc="Delay"; parInfoMExpDe[0].scale=stfnum::xscale; parInfoMExpDe[0].unscale=stfnum::xunscale;
    parInfoMExpDe[2].toFit=true; parInfoMExpDe[2].desc="tau"; parInfoMExpDe[0].scale=stfnum::xscale; parInfoMExpDe[0].unscale=stfnum::xunscale;
    parInfoMExpDe[3].toFit=true; parInfoMExpDe[3].desc="Peak"; parInfoMExpDe[0].scale=stfnum::yscale; parInfoMExpDe[0].unscale=stfnum::yunscale;
    funcList.push_back(stfnum::storedFunc("Monoexponential with delay, start fixed to baseline",
                                         parInfoMExpDe,fexpde,fexpde_init,stfnum::nojac,false));

    // Biexponential function, free fit:
    std::vector<stfnum::parInfo> parInfoBExp=getParInfoExp(2);
    funcList.push_back(stfnum::storedFunc(
                                       "Biexponential",parInfoBExp,fexp,fexp_init,fexp_jac,true,outputWTau));

    // Biexponential function, offset fixed to baseline:
    parInfoBExp[4].toFit=false;
    funcList.push_back(stfnum::storedFunc("Biexponential, offset fixed to baseline",
                                         parInfoBExp,fexp,fexp_init,fexp_jac,true,outputWTau));

    // Biexponential function, starting with a delay, start fixed to baseline:
    std::vector<stfnum::parInfo> parInfoBExpDe(5);
    parInfoBExpDe[0].toFit=false; parInfoBExpDe[0].desc="Baseline"; parInfoBExpDe[0].scale=stfnum::yscaleoffset; parInfoBExpDe[0].unscale=stfnum::yunscaleoffset;
    parInfoBExpDe[1].toFit=true;  parInfoBExpDe[1].desc="Delay"; parInfoBExpDe[1].scale=stfnum::xscale; parInfoBExpDe[1].unscale=stfnum::xunscale; 
    // parInfoBExpDe[1].constrained = true; parInfoBExpDe[1].constr_lb = 0.0; parInfoBExpDe[1].constr_ub = DBL_MAX;
    parInfoBExpDe[2].toFit=true;  parInfoBExpDe[2].desc="tau1"; parInfoBExpDe[2].scale=stfnum::xscale; parInfoBExpDe[2].unscale=stfnum::xunscale;
    // parInfoBExpDe[2].constrained = true; parInfoBExpDe[2].constr_lb = 1.0e-16; parInfoBExpDe[2].constr_ub = DBL_MAX;
    parInfoBExpDe[3].toFit=true;  parInfoBExpDe[3].desc="Factor"; parInfoBExpDe[3].scale=stfnum::yscale; parInfoBExpDe[3].unscale=stfnum::yunscale;
    parInfoBExpDe[4].toFit=true;  parInfoBExpDe[4].desc="tau2"; parInfoBExpDe[4].scale=stfnum::xscale; parInfoBExpDe[4].unscale=stfnum::xunscale;
    // parInfoBExpDe[4].constrained = true; parInfoBExpDe[4].constr_lb = 1.0e-16; parInfoBExpDe[4].constr_ub = DBL_MAX;
    funcList.push_back(stfnum::storedFunc(
                                       "Biexponential with delay, start fixed to baseline, delay constrained to > 0",
                                       parInfoBExpDe,fexpbde,fexpbde_init,stfnum::nojac,false));

    // Triexponential function, free fit:
    std::vector<stfnum::parInfo> parInfoTExp=getParInfoExp(3);
    funcList.push_back(stfnum::storedFunc(
                                       "Triexponential",parInfoTExp,fexp,fexp_init,fexp_jac,true,outputWTau));

    // Triexponential function, free fit, different initialization:
    funcList.push_back(stfnum::storedFunc(
                                       "Triexponential, initialize for PSCs/PSPs",parInfoTExp,fexp,fexp_init2,fexp_jac,true,outputWTau));

    // Triexponential function, offset fixed to baseline:
    parInfoTExp[6].toFit=false;
    funcList.push_back(stfnum::storedFunc(
                                       "Triexponential, offset fixed to baseline",parInfoTExp,fexp,fexp_init,fexp_jac,true,outputWTau));

    // Alpha function:
    std::vector<stfnum::parInfo> parInfoAlpha(3);
    parInfoAlpha[0].toFit=true; parInfoAlpha[0].desc="Amplitude";
    parInfoAlpha[1].toFit=true; parInfoAlpha[1].desc="Rate";
    parInfoAlpha[2].toFit=true; parInfoAlpha[2].desc="Offset";
    funcList.push_back(stfnum::storedFunc(
                                       "Alpha function", parInfoAlpha,falpha,falpha_init,falpha_jac,true));

    // HH gNa function:
    std::vector<stfnum::parInfo> parInfoHH(4);
    parInfoHH[0].toFit=true; parInfoHH[0].desc="gprime_na";
    parInfoHH[1].toFit=true; parInfoHH[1].desc="tau_m";
    parInfoHH[2].toFit=true; parInfoHH[2].desc="tau_h";
    parInfoHH[3].toFit=false; parInfoHH[3].desc="offset";
    funcList.push_back(stfnum::storedFunc(
                                         "Hodgkin-Huxley g_Na function, offset fixed to baseline", parInfoHH, fHH, fHH_init, stfnum::nojac, false));

    // power of 1 gNa function:
    funcList.push_back(stfnum::storedFunc(
                                         "power of 1 g_Na function, offset fixed to baseline", parInfoHH, fgnabiexp, fgnabiexp_init, fgnabiexp_jac, true));

    // Gaussian
    std::vector<stfnum::parInfo> parInfoGauss(3);
    parInfoGauss[0].toFit=true; parInfoGauss[0].desc="amp"; parInfoGauss[0].scale = stfnum::yscale; parInfoGauss[0].unscale = stfnum::yunscale;
    parInfoGauss[1].toFit=true; parInfoGauss[1].desc="mean"; parInfoGauss[1].scale = stfnum::xscale; parInfoGauss[1].unscale = stfnum::xunscale;

    parInfoGauss[2].toFit=true;
    parInfoGauss[2].constrained=true; parInfoGauss[2].constr_lb=0; parInfoGauss[2].constr_ub=DBL_MAX;
    parInfoGauss[2].desc="width"; parInfoGauss[2].scale = stfnum::xscale; parInfoGauss[2].unscale = stfnum::xunscale;

    funcList.push_back(stfnum::storedFunc(
                                       "Gaussian", parInfoGauss, fgauss, fgauss_init, fgauss_jac, true));

    // Triexponential function, starting with a delay, start fixed to baseline:
    std::vector<stfnum::parInfo> parInfoTExpDe(7);
    parInfoTExpDe[0].toFit=false; parInfoTExpDe[0].desc="Baseline"; parInfoTExpDe[0].scale=stfnum::yscaleoffset; parInfoTExpDe[0].unscale=stfnum::yunscaleoffset;
    parInfoTExpDe[1].toFit=true;  parInfoTExpDe[1].desc="Delay"; parInfoTExpDe[1].scale=stfnum::xscale; parInfoTExpDe[1].unscale=stfnum::xunscale; 
    // parInfoTExpDe[1].constrained = true; parInfoTExpDe[1].constr_lb = 0.0; parInfoTExpDe[1].constr_ub = DBL_MAX;
    parInfoTExpDe[2].toFit=true;  parInfoTExpDe[2].desc="tau1a"; parInfoTExpDe[2].scale=stfnum::xscale; parInfoTExpDe[2].unscale=stfnum::xunscale;
    // parInfoTExpDe[2].constrained = true; parInfoTExpDe[2].constr_lb = 1.0e-16; parInfoTExpDe[2].constr_ub = DBL_MAX;
    parInfoTExpDe[3].toFit=true;  parInfoTExpDe[3].desc="Factor"; parInfoTExpDe[3].scale=stfnum::yscale; parInfoTExpDe[3].unscale=stfnum::yunscale;
    parInfoTExpDe[4].toFit=true;  parInfoTExpDe[4].desc="tau2"; parInfoTExpDe[4].scale=stfnum::xscale; parInfoTExpDe[4].unscale=stfnum::xunscale;
    parInfoTExpDe[5].toFit=true;  parInfoTExpDe[5].desc="tau1b"; parInfoTExpDe[5].scale=stfnum::xscale; parInfoTExpDe[5].unscale=stfnum::xunscale;
    parInfoTExpDe[6].toFit=true;  parInfoTExpDe[6].desc="ptau1b"; parInfoTExpDe[6].scale=stfnum::noscale; parInfoTExpDe[6].unscale=stfnum::noscale;
    funcList.push_back(stfnum::storedFunc(
                                       "Triexponential with delay, start fixed to baseline, delay constrained to > 0",
                                       parInfoTExpDe,fexptde,fexptde_init,stfnum::nojac,false));

    return funcList;
}

double stfnum::fexp(double x, const Vector_double& p) {
    double sum=0.0;
    for (std::size_t n_p=0;n_p<p.size()-1;n_p+=2) {
        double e=exp(-x/p[n_p+1]);
        sum+=p[n_p]*e;
    }
    return sum+p[p.size()-1];
}

Vector_double stfnum::fexp_jac(double x, const Vector_double& p) {
    Vector_double jac(p.size());
    for (std::size_t n_p=0;n_p<p.size()-1;n_p+=2) {
        double e=exp(-x/p[n_p+1]);
        jac[n_p]=e;
        jac[n_p+1]=p[n_p]*x*e/(p[n_p+1]*p[n_p+1]);
    }
    jac[p.size()-1]=1.0;
    return jac;
}

void stfnum::fexp_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find out direction:
    bool increasing = data[0] < data[data.size()-1];
    Vector_double::const_iterator max_el = std::max_element(data.begin(), data.end());
    Vector_double::const_iterator min_el = std::min_element(data.begin(), data.end());
    double floor = (increasing ? (*max_el+1.0e-9) : (*min_el-1.0e-9));
    Vector_double peeled( stfio::vec_scal_minus(data, floor));
    if (increasing) peeled = stfio::vec_scal_mul(peeled, -1.0);
    std::transform(peeled.begin(), peeled.end(), peeled.begin(),
#if defined(_MSC_VER)
                   std::logl);
#elif defined(__clang__)
                   std::logl);
#else	// defined(__GNUC__)  // all gcc-based compilers including mingw
                   log);
#endif

    // linear fit on log-transformed data:
    Vector_double x(data.size());
    for (std::size_t n_x = 0; n_x < x.size(); ++n_x) {
        x[n_x] = (double)n_x * dt;
    }
    double m=0, c=0;
    stfnum::linFit(x,peeled,m,c);
    
    double tau_mean = -1.0 / m;

    int n_exp=(int)pInit.size()/2;

    // Distribute taus:
    for (int n_p = 0; n_p < (int)pInit.size()-2; n_p+=2) {
        int n_term = n_p/2 + 1;
        double frac = pow((double)n_term,3) / pow((((double)n_exp+1.0)/2.0),3);
        // Calculate tau and amplitude:
        pInit[n_p+1] = tau_mean * frac;
    }
    // Estimate amps:
    double amp_total = data[0]-data[data.size()-1];
    for (int n_p = 0; n_p < (int)pInit.size()-2; n_p+=2) {
        pInit[n_p] = amp_total / n_exp;
    }
    // offset:
    pInit[pInit.size()-1] = data[data.size()-1];

}

void stfnum::fexp_init2(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    int n_exp=(int)pInit.size()/2;
    for (std::size_t n_p=0;n_p<pInit.size()-1;n_p+=2) {
        // use inverse amplitude for last term:
        int sign=1;
        if ((int)n_p==n_exp*2-2) {
            sign=-1;
        }
        pInit[n_p]=(double)sign/(double)n_exp*fabs(peak-base);
        pInit[n_p+1]=1.0/((double)n_p+2.0)/((double)n_p+2.0)*(double)data.size()*dt;
    }
    pInit[pInit.size()-1]=peak;
}

double stfnum::xscale(double param, double xscale, double xoff, double yscale, double yoff) {
    return param*xscale; // + xoff;
}

double stfnum::xunscale(double param, double xscale, double xoff, double yscale, double yoff) {
    return param/xscale; //(param-xoff)/xscale;
}

double stfnum::yscale(double param, double xscale, double xoff, double yscale, double yoff) {
    return param*yscale;
}

double stfnum::yscaleoffset(double param, double xscale, double xoff, double yscale, double yoff) {
    return param*yscale - yoff;
}

double stfnum::yunscale(double param, double xscale, double xoff, double yscale, double yoff) {
    return param/yscale;
}

double stfnum::yunscaleoffset(double param, double xscale, double xoff, double yscale, double yoff) {
    return (param+yoff)/yscale;
}

double stfnum::fexpde(double x, const Vector_double& p) {
    if (x<p[1]) {
        return p[0];
    } else {
        double e1=exp((p[1]-x)/p[2]);
        // normalize the amplitude so that the peak really is the peak:
        return (p[0]-p[3])*e1 + p[3];
    }
}

#if 0
Vector_double stfnum::fexpde_jac(double x, const Vector_double& p) {
    Vector_double jac(4);
    if (x<p[3]) {
        jac[0]=1.0;
        jac[1]=0.0;
        jac[2]=0.0;
        jac[3]=0.0;
    } else {
        double e=exp((p[3]-x)/p[1]);
        jac[0]=e;
        jac[1]=(p[0]-p[2])*(p[3]-x)*(-1.0/(p[1]*p[1]))*e;
        jac[2]=-e+1.0;
        jac[3]=(p[0]-p[2])*(1.0/p[1])*e;
    }
    return jac;
}
#endif 

void stfnum::fexpde_init(const Vector_double& data, double base, double peak, double RTLoHI, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find the peak position in data:
    double maxT;
    stfnum::peak( data, base, 0, data.size()-1, 1, stfnum::both, maxT );

    pInit[0]=base;
    pInit[1]=0.0;
    pInit[2]=0.5 * maxT * dt;
    pInit[3]=peak;
}

double stfnum::fexpbde(double x, const Vector_double& p) {
    if (x<p[1]) {
        return p[0];
    } else {
        // double tpeak = p[4]*p[2]*log(p[4]/p[2])/(p[4]-p[2]);
        // double adjust = 1.0/((1.0-exp(-tpeak/p[4]))-(1.0-exp(-tpeak/p[2])));
        double e1=exp((p[1]-x)/p[2]);
        double e2=exp((p[1]-x)/p[4]);

        return p[3]*e1 - p[3]*e2 + p[0];
    }
}

double stfnum::fexptde(double x, const Vector_double& p) {
    if (x<p[1]) {
        return p[0];
    } else {
        // double tpeak = p[4]*p[2]*log(p[4]/p[2])/(p[4]-p[2]);
        // double adjust = 1.0/((1.0-exp(-tpeak/p[4]))-(1.0-exp(-tpeak/p[2])));
        double e1=exp((p[1]-x)/p[2]);
        double e2=exp((p[1]-x)/p[4]);
        double e3=exp((p[1]-x)/p[5]);

        return p[6]*p[3]*e1 + (1.0-p[6])*p[3]*e3 - p[3]*e2 + p[0];
    }
}

#if 0
Vector_double stfnum::fexpbde_jac(double x, const Vector_double& p) {
    Vector_double jac(5);
    if (x<p[1]) {
        jac[0]=1.0;
        jac[1]=0.0;
        jac[2]=0.0;
        jac[3]=0.0;
        jac[4]=0.0;
    } else {
        double tpeak = p[4]*p[2]*log(p[4]/p[2])/(p[4]-p[2]);
        double adjust = 1.0/((1.0-exp(-tpeak/p[4]))-(1.0-exp(-tpeak/p[2])));
        double e1=exp((p[1]-x)/p[2]);
        double e2=exp((p[1]-x)/p[4]);
        jac[0]=1.0;
        jac[1]=adjust*p[3]/p[2] * e1 - adjust*p[3]/p[4] * e2;
        jac[2]=adjust*p[3]*(p[1]-x)*(-1.0/(p[2]*p[2]))*e1;
        jac[3]=adjust*e1-adjust*e2;
        jac[4]=adjust*p[3]*(p[1]-x)*(1.0/(p[4]*p[4]))*e2;
    }
    return jac;
}
#endif

void stfnum::fexpbde_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find the peak position in data:
    double maxT = stfnum::whereis( data, peak );

    if ( maxT == 0 ) maxT = data.size() * 0.05;

    pInit[0] = base; /* baseline */
    //pInit[1] = 0.01;
    //pInit[1] = 1.0; /* latency */
    // Use the left fitting cursor to estimate latency
    pInit[1] = maxT * dt; /* latency */
    //pInit[2] = 3 * maxT * dt; /* tau1 time constant */
    pInit[2] = 1.5*HalfWidth; /* tau1 time constant */
    //pInit[4] = 0.5 * maxT * dt; /* tau2 time constant */
    pInit[4] = RTLoHi; /* tau2 time constant */
    double tpeak = pInit[4]*pInit[2]*log(pInit[4]/pInit[2])/(pInit[4]-pInit[2]);
    double adjust = 1.0/((1.0-exp(-tpeak/pInit[4]))-(1.0-exp(-tpeak/pInit[2])));
    pInit[3] = adjust*(peak-base); /* factor */

}

void stfnum::fexptde_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find the peak position in data:
    double maxT = stfnum::whereis( data, peak );

    if ( maxT == 0 ) maxT = data.size() * 0.05;

    pInit[0] = base; /* baseline */
    //pInit[1] = 0.01;
    //pInit[1] = 1.0; /* latency */
    // Use the left fitting cursor to estimate latency
    pInit[1] = maxT * dt; /* latency */
    //pInit[2] = 3 * maxT * dt; /* tau1 time constant */
    pInit[2] = 1.5*HalfWidth; /* tau1a time constant */
    pInit[5] = 1.5*HalfWidth; /* tau1b time constant */
    //pInit[4] = 0.5 * maxT * dt; /* tau2 time constant */
    pInit[4] = RTLoHi; /* tau2 time constant */
    double tpeak = pInit[4]*pInit[2]*log(pInit[4]/pInit[2])/(pInit[4]-pInit[2]);
    double adjust = 1.0/((1.0-exp(-tpeak/pInit[4]))-(1.0-exp(-tpeak/pInit[2])));
    pInit[3] = adjust*(peak-base); /* factor */
    pInit[6] = 0.5;
}

double stfnum::falpha(double x, const Vector_double& p) {
    
    //double e=exp(-p[1]*x);
    //return p[0]*p[1]*p[1]*x*e+p[2]; 
    return p[0]*x/p[1]*exp(1-x/p[1]) + p[2];
    
}

Vector_double stfnum::falpha_jac(double x, const Vector_double& p) {
    Vector_double jac(3);
    //double e=exp(-p[1]*x);
    //jac[0]=p[1]*p[1]*x*e;
    //jac[1]=p[0]*x*p[1]*(2*e-x*p[1]*e);
    //jac[2]=1.0;
    jac[0] = x*exp(1-x/p[1])/p[1];
    jac[1] = jac[0]*( x*p[0]/(p[1]*p[1]) - p[0]/p[1] );
    jac[2] = 1.0;
    return jac;
}

void stfnum::falpha_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
        double maxT = stfnum::whereis( data, peak )*dt;

        pInit[0] = peak;
        pInit[1] = maxT;// time of the peak correspond to time constant
        pInit[2] = base;

        //pInit[0]=(peak-base)*data.size()*dt;
        //pInit[1]=1.0/(data.size()*dt/20.0);
        //pInit[2]=base;
}

double stfnum::fHH(double x, const Vector_double& p) {
    // p[0]: gprime_na
    // p[1]: tau_m
    // p[2]: tau_h
    // p[3]: offset
    double m = 1 - exp(-x/p[1]);
    double h = exp(-x/p[2]);
    return p[0] * (m*m*m) * h + p[3];
}

double stfnum::fgnabiexp(double x, const Vector_double& p) {
    // p[0]: gprime_na
    // p[1]: tau_m
    // p[2]: tau_h
    // p[3]: offset
    double m = 1-exp(-x/p[1]);
    double h = exp(-x/p[2]);
    return p[0] * m * h + p[3];
}

double stfnum::fgauss(double x, const Vector_double& pars) {
    double y=0.0, /* fac=0.0, */ ex=0.0, arg=0.0;
    int npars=static_cast<int>(pars.size());
    for (int i=0; i < npars-1; i += 3) {
        arg=(x-pars[i+1])/pars[i+2];
        ex=exp(-arg*arg);
        /* fac=pars[i]*ex*2.0*arg; */
        y += pars[i] * ex;
    }
    return y;
}

Vector_double stfnum::fgauss_jac(double x, const Vector_double& pars) {
    double ex=0.0, arg=0.0;
    int npars=static_cast<int>(pars.size());
    Vector_double jac(npars);
    for (int i=0; i < npars-1; i += 3) {
        arg=(x-pars[i+1])/pars[i+2];
        ex=exp(-arg*arg);
        jac[i] = ex;
        jac[i+1] = 2.0*ex*pars[i]*(x-pars[i+1]) / (pars[i+2]*pars[i+2]);
        jac[i+2] = 2.0*ex*pars[i]*(x-pars[i+1])*(x-pars[i+1]) / (pars[i+2]*pars[i+2]*pars[i+2]);
    }
    return jac;
}

void stfnum::fgauss_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find the peak position in data:
    double maxT = stfnum::whereis( data, peak ) * dt;
    int npars=static_cast<int>(pInit.size());
    for (int i=0; i < npars-1; i += 3) {
        pInit[i] = peak;
        pInit[i+1] = maxT;
        pInit[i+2] = HalfWidth/ 1.65; //approximate t50 to one standard deviation
    }
}

void stfnum::fHH_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find the peak position in data:
    double maxT = stfnum::whereis( data, peak );
    
    if ( maxT == 0 ) maxT = data.size() * 0.05;

    // p[0]: gprime_na
    // p[1]: tau_m
    // p[2]: tau_h
    // p[3]: offset
    pInit[1] = RTLoHi;
    pInit[2] = HalfWidth;
    pInit[3] = base; //offset fixed to baseline

    double norm = (27.0*pow(pInit[2],3)*exp(-(pInit[1]*log((3.0*pInit[2]+pInit[1])/pInit[1]))/pInit[2])) / 
                  (27.0*pow(pInit[2],3)+27.0*pInit[1]*pInit[2]*pInit[2]+9.0*pInit[1]*pInit[1]*pInit[2]+pow(pInit[1],3));

    pInit[0] = (peak-base)/norm;
    //pInit[1] = 0.5 * maxT * dt;
    //pInit[2] = 3 * maxT * dt;
}

Vector_double stfnum::fgnabiexp_jac(double x, const Vector_double& p) {
    Vector_double jac(4);
    jac[0] = ( 1-exp(-x/p[1]) ) * exp(-x/p[2]);
    jac[1] = -p[0] * x * exp(-x/p[1] - x/p[2])  /(p[1]*p[1]);
    jac[2] = p[0] * x * ( 1-exp(-x/p[1]) ) * exp(-x/p[2]) / (p[2]*p[2]);
    jac[3] = 1.0;
    return jac;
}

void stfnum::fgnabiexp_init(const Vector_double& data, double base, double peak, double RTLoHi, double HalfWidth, double dt, Vector_double& pInit ) {
    // Find the peak position in data:
    double maxT = stfnum::whereis( data, peak );
    
    if ( maxT == 0 ) maxT = data.size() * 0.05;
    // p[0]: gprime_na
    // p[1]: tau_m
    // p[2]: tau_h
    // p[3]: offset
    // pInit[1]=0.5 * maxT * dt;
    // pInit[2]=3 * maxT * dt;
    pInit[1] = RTLoHi;
    pInit[2] = HalfWidth;
    pInit[3] = base; // offset fixed to baseline

    double tpeak = pInit[1]*log(pInit[2]/pInit[1]+1);
    double norm = (1-exp(-tpeak/pInit[1]))*exp(-tpeak/pInit[2]);
    pInit[0] = (peak-base)/norm;
}

std::vector<stfnum::parInfo> stfnum::getParInfoExp(int n_exp) {
    std::vector<stfnum::parInfo> retParInfo(n_exp*2+1);
    for (int n_e=0; n_e<n_exp*2; n_e+=2) {
        retParInfo[n_e].toFit=true;
        std::ostringstream adesc;
        adesc << "Amp_" << (int)n_e/2;
        retParInfo[n_e].desc = adesc.str();
        retParInfo[n_e].scale = stfnum::yscale;
        retParInfo[n_e].unscale = stfnum::yunscale;
        retParInfo[n_e+1].toFit=true;
        std::ostringstream tdesc;
        tdesc  <<  "Tau_" << (int)n_e/2;
        retParInfo[n_e+1].desc = tdesc.str();
        retParInfo[n_e+1].scale = stfnum::xscale;
        retParInfo[n_e+1].unscale = stfnum::xunscale;
    }
    retParInfo[n_exp*2].toFit=true;
    retParInfo[n_exp*2].desc="Offset";
    retParInfo[n_exp*2].scale=stfnum::yscaleoffset;
    retParInfo[n_exp*2].unscale=stfnum::yunscaleoffset;
    return retParInfo;
}

stfnum::Table stfnum::outputWTau(
    const Vector_double& pars,
    const std::vector<stfnum::parInfo>& parsInfo,
    double chisqr
) {
    stfnum::Table output(pars.size()+1,1);
    // call default version:
    try  {
        output=defaultOutput(pars,parsInfo,chisqr);
    }
    catch (...) {
        throw;
    }
    // add weighted tau:
    // sum up amplitude terms:
    double sumAmp=0.0;
    for (std::size_t n_p=0;n_p<pars.size()-1;n_p+=2) {
        sumAmp+=pars[n_p];
    }
    // weight taus by their respective amplitudes:
    double sumTau=0.0;
    for (std::size_t n_p=0;n_p<pars.size()-1;n_p+=2) {
        sumTau+=(pars[n_p]/sumAmp)*pars[n_p+1];
    }
    // print:
    output.AppendRows(1);
    try {
        output.SetRowLabel(pars.size()+1, "Weighted tau");
        output.at(pars.size()+1,0)=sumTau;
    }
    catch (...) {
        throw;
    }
    return output;
}

std::size_t stfnum::whereis(const Vector_double& data, double value) {
    if (data.size()==0) return 0;
    bool fromtop=false;
    // coming from top or bottom?
    if (data[0]>value) {
        fromtop=true;
    }
    for (std::size_t n=0;n<data.size();++n) {
        if (fromtop) {
            if (data[n] <= value ) {
                return n;
            }
        } else {
            if (data[n] >= value) {
                return n;
            }
        }
    }
    return 0;
}

