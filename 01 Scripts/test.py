import pandas as pd

df_contribution = pd.DataFrame(
    {
     'Package': list_master_package_name,
     'Login':list_contributor_login_final,
     'Id':list_contributor_id_final,
     'Contributions':list_contributor_contributions_final,
    })
df_contribution.to_csv(f"df_contribution_{str(j-1)}.csv",index=False)