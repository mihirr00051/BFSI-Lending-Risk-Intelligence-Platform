library(readr)
library(dplyr)
library(ggplot2)
root <- normalizePath(file.path(getwd()))
loans <- read_csv(file.path(root,'data/raw/loans.csv'), show_col_types=FALSE)
customers <- read_csv(file.path(root,'data/raw/customers.csv'), show_col_types=FALSE)

portfolio <- loans %>%
  left_join(customers, by='customer_id') %>%
  group_by(segment, product) %>%
  summarise(
    loans=n(),
    aum=sum(outstanding_principal),
    avg_rate=mean(interest_rate),
    delinquency_rate=mean(dpd>0),
    npl_proxy_rate=mean(dpd>=90),
    .groups='drop')

print(portfolio %>% arrange(desc(aum)))

g <- ggplot(portfolio, aes(x=reorder(product,aum), y=aum, fill=segment)) +
  geom_col(position='dodge') + coord_flip() +
  labs(title='BFSI Loan Portfolio by Product and Segment', x=NULL, y='AUM')
print(g)
