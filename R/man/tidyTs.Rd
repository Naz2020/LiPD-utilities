% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/tidy2.R
\name{tidyTs}
\alias{tidyTs}
\title{create tidy data.frame from TS (old version)}
\usage{
tidyTs(TS, age.var = "age")
}
\arguments{
\item{TS}{a LiPD Timeseries object}

\item{age.var}{}
}
\value{
a tidy data.frame
}
\description{
Deprecated. The new version `tidyTs()` is *much* faster. takes a TS object and turns it into a long, tidy, data.frame. Useful for data manipulation and analysis in the tidyverse and plotting
}
\seealso{
Other LiPD manipulation: 
\code{\link{pullTsVariable}()},
\code{\link{pushTsVariable}()},
\code{\link{tidyTsOld}()}
}
\concept{LiPD manipulation}
