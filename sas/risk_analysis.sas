/* SAS Data and AI Studio / SAS Viya compatible analytical example */
proc import datafile="data/raw/loans.csv" out=work.loans dbms=csv replace;
    guessingrows=max; getnames=yes;
run;

proc format;
  value dpdband 0='Current' 1-30='1-30 DPD' 31-60='31-60 DPD' 61-90='61-90 DPD' 91-high='90+ DPD';
run;

data work.loan_risk;
  set work.loans;
  length risk_band $12;
  if dpd=0 then risk_band='Current';
  else if dpd <=30 then risk_band='Early';
  else if dpd <=90 then risk_band='Watch';
  else risk_band='NPL';
run;

proc sql;
  create table work.portfolio_risk as
  select product,
         count(*) as loans,
         sum(outstanding_principal) as aum,
         mean(dpd>0) as delinquency_rate,
         mean(dpd>=90) as npl_proxy_rate
  from work.loan_risk
  group by product
  order by npl_proxy_rate desc;
quit;

proc means data=work.loan_risk n mean median p25 p75;
  var outstanding_principal interest_rate dpd;
run;
