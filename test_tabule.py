from tabula import read_pdf

dfs_list = read_pdf("jurados.pdf", pages="1", stream=True)

print(len(dfs_list))
dfs_list[0].to_csv("output_tabula.csv", index=False)