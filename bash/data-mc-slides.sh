#!/bin/bash

[[ -f $1 ]] && rm $1

cat >> $1 <<EOF
\documentclass[9pt]{beamer}
\usetheme{boxes}
\usecolortheme{orchid}
\usecolortheme[RGB={70,70,70}]{structure}
\usefonttheme{structurebold}
\setbeamertemplate{footline}[frame number]
\beamertemplatenavigationsymbolsempty
%--------------------------------------------------
\newenvironment{changemargin}[2]{%
  \begin{list}{}{
    \setlength{\topsep}{0pt}%
    \setlength{\leftmargin}{#1}%
    \setlength{\rightmargin}{#2}%
    \setlength{\listparindent}{\parindent}%
    \setlength{\itemindent}{\parindent}%
    \setlength{\parsep}{\parskip}%
  }%
  \item[]}{\end{list}}
%--------------------------------------------------Titlepage
\title{Data/MC}
\subtitle{Strong 1L selections}
\author{Eric Schanet}
\institute{LMU Munich}
\date{\today}
%--------------------------------------------------Begin
\begin{document}
\maketitle
EOF

input=$2
#for sample in ttbar singletop wjets zjets diboson ttv data
# for d in strong1L_presel strong1L_presel_electron strong1L_presel_muon strong1L_TR2J strong1L_TR4Jhighx strong1L_TR4Jlowx strong1L_TR6J strong1L_VR2Jmet strong1L_VR2JmetBT strong1L_VR2JmetBT_bin1 strong1L_VR2JmetBT_bin2 strong1L_VR2JmetBT_bin3 strong1L_VR2JmetBT_bin4 strong1L_VR2JmetBV strong1L_VR2Jmt strong1L_VR2JmtBT strong1L_VR2JmtBV strong1L_VR2JmtBVsecondbin strong1L_VR2JmtBVthirdbin strong1L_VR2Jnomet strong1L_VR2Jnomt strong1L_VR4Jhighxapl strong1L_VR4JhighxaplBT strong1L_VR4JhighxaplBV strong1L_VR4Jhighxhybrid strong1L_VR4JhighxhybridBT strong1L_VR4JhighxhybridBV strong1L_VR4Jhighxmt strong1L_VR4JhighxmtBT strong1L_VR4JhighxmtBV strong1L_VR4Jhighxnoapl strong1L_VR4Jhighxnoapl_bin1 strong1L_VR4Jhighxnoapl_bin2 strong1L_VR4Jhighxnoapl_bin3 strong1L_VR4Jhighxnomt strong1L_VR4Jlowxapl strong1L_VR4JlowxaplBT strong1L_VR4JlowxaplBV strong1L_VR4JlowxaplBV_bin1 strong1L_VR4JlowxaplBV_bin2 strong1L_VR4JlowxaplBV_bin3 strong1L_VR4Jlowxhybrid strong1L_VR4JlowxhybridBT strong1L_VR4JlowxhybridBV strong1L_VR4Jlowxnoapl strong1L_VR4Jlowxnomt strong1L_VR6Japl strong1L_VR6JaplBT strong1L_VR6JaplBV strong1L_VR6Jmt strong1L_VR6JmtBT strong1L_VR6JmtBV strong1L_VR6Jnoapl strong1L_VR6Jnomt strong1L_WR2J strong1L_WR4Jhighx strong1L_WR4Jlowx strong1L_WR6J; do

for d in strong1L_presel strong1L_presel_electron strong1L_presel_muon strong1L_TR2J_bin1 strong1L_TR2J_bin2 strong1L_TR2J_bin3 strong1L_TR2J_bin4 strong1L_TR4Jhighx_bin1 strong1L_TR4Jhighx_bin2 strong1L_TR4Jhighx_bin3 strong1L_TR4Jlowx_bin1 strong1L_TR4Jlowx_bin2 strong1L_TR4Jlowx_bin3 strong1L_TR6J_bin1 strong1L_TR6J_bin2 strong1L_TR6J_bin3 strong1L_TR6J_bin4 strong1L_VR2Jmet_bin1 strong1L_VR2Jmet_bin2 strong1L_VR2Jmet_bin3 strong1L_VR2Jmet_bin4 strong1L_VR2JmetBT_bin1 strong1L_VR2JmetBT_bin2 strong1L_VR2JmetBT_bin3 strong1L_VR2JmetBT_bin4 strong1L_VR2JmetBV_bin1 strong1L_VR2JmetBV_bin2 strong1L_VR2JmetBV_bin3 strong1L_VR2JmetBV_bin4 strong1L_VR2Jmt_bin1 strong1L_VR2Jmt_bin2 strong1L_VR2Jmt_bin3 strong1L_VR2Jmt_bin4 strong1L_VR2JmtBT_bin1 strong1L_VR2JmtBT_bin2 strong1L_VR2JmtBT_bin3 strong1L_VR2JmtBT_bin4 strong1L_VR2JmtBV_bin1 strong1L_VR2JmtBV_bin2 strong1L_VR2JmtBV_bin3 strong1L_VR2JmtBV_bin4 strong1L_VR2Jnomet_bin1 strong1L_VR2Jnomet_bin2 strong1L_VR2Jnomet_bin3 strong1L_VR2Jnomet_bin4 strong1L_VR2Jnomt_bin1 strong1L_VR2Jnomt_bin2 strong1L_VR2Jnomt_bin3 strong1L_VR2Jnomt_bin4 strong1L_VR4Jhighxapl_bin1 strong1L_VR4Jhighxapl_bin2 strong1L_VR4Jhighxapl_bin3 strong1L_VR4JhighxaplBT_bin1 strong1L_VR4JhighxaplBT_bin2 strong1L_VR4JhighxaplBT_bin3 strong1L_VR4JhighxaplBV_bin1 strong1L_VR4JhighxaplBV_bin2 strong1L_VR4JhighxaplBV_bin3 strong1L_VR4Jhighxhybrid_bin1 strong1L_VR4Jhighxhybrid_bin2 strong1L_VR4Jhighxhybrid_bin3 strong1L_VR4JhighxhybridBT_bin1 strong1L_VR4JhighxhybridBT_bin2 strong1L_VR4JhighxhybridBT_bin3 strong1L_VR4JhighxhybridBV_bin1 strong1L_VR4JhighxhybridBV_bin2 strong1L_VR4JhighxhybridBV_bin3 strong1L_VR4Jhighxmt_bin1 strong1L_VR4Jhighxmt_bin2 strong1L_VR4Jhighxmt_bin3 strong1L_VR4JhighxmtBT_bin1 strong1L_VR4JhighxmtBT_bin2 strong1L_VR4JhighxmtBT_bin3 strong1L_VR4JhighxmtBV_bin1 strong1L_VR4JhighxmtBV_bin2 strong1L_VR4JhighxmtBV_bin3 strong1L_VR4Jhighxnoapl_bin1 strong1L_VR4Jhighxnoapl_bin2 strong1L_VR4Jhighxnoapl_bin3 strong1L_VR4Jhighxnomt_bin1 strong1L_VR4Jhighxnomt_bin2 strong1L_VR4Jhighxnomt_bin3 strong1L_VR4Jlowxapl_bin1 strong1L_VR4Jlowxapl_bin2 strong1L_VR4Jlowxapl_bin3 strong1L_VR4JlowxaplBT_bin1 strong1L_VR4JlowxaplBT_bin2 strong1L_VR4JlowxaplBT_bin3 strong1L_VR4JlowxaplBV_bin1 strong1L_VR4JlowxaplBV_bin2 strong1L_VR4JlowxaplBV_bin3 strong1L_VR4Jlowxhybrid_bin1 strong1L_VR4Jlowxhybrid_bin2 strong1L_VR4Jlowxhybrid_bin3 strong1L_VR4JlowxhybridBT_bin1 strong1L_VR4JlowxhybridBT_bin2 strong1L_VR4JlowxhybridBT_bin3 strong1L_VR4JlowxhybridBV_bin1 strong1L_VR4JlowxhybridBV_bin2 strong1L_VR4JlowxhybridBV_bin3 strong1L_VR4Jlowxnoapl_bin1 strong1L_VR4Jlowxnoapl_bin2 strong1L_VR4Jlowxnoapl_bin3 strong1L_VR4Jlowxnomt_bin1 strong1L_VR4Jlowxnomt_bin2 strong1L_VR4Jlowxnomt_bin3 strong1L_VR6Japl_bin1 strong1L_VR6Japl_bin2 strong1L_VR6Japl_bin3 strong1L_VR6Japl_bin4 strong1L_VR6JaplBT_bin1 strong1L_VR6JaplBT_bin2 strong1L_VR6JaplBT_bin3 strong1L_VR6JaplBT_bin4 strong1L_VR6JaplBV_bin1 strong1L_VR6JaplBV_bin2 strong1L_VR6JaplBV_bin3 strong1L_VR6JaplBV_bin4 strong1L_VR6Jmt_bin1 strong1L_VR6Jmt_bin2 strong1L_VR6Jmt_bin3 strong1L_VR6Jmt_bin4 strong1L_VR6JmtBT_bin1 strong1L_VR6JmtBT_bin2 strong1L_VR6JmtBT_bin3 strong1L_VR6JmtBT_bin4 strong1L_VR6JmtBV_bin1 strong1L_VR6JmtBV_bin2 strong1L_VR6JmtBV_bin3 strong1L_VR6JmtBV_bin4 strong1L_VR6Jnoapl_bin1 strong1L_VR6Jnoapl_bin2 strong1L_VR6Jnoapl_bin3 strong1L_VR6Jnoapl_bin4 strong1L_VR6Jnomt_bin1 strong1L_VR6Jnomt_bin2 strong1L_VR6Jnomt_bin3 strong1L_VR6Jnomt_bin4 strong1L_WR2J_bin1 strong1L_WR2J_bin2 strong1L_WR2J_bin3 strong1L_WR2J_bin4 strong1L_WR4Jhighx_bin1 strong1L_WR4Jhighx_bin2 strong1L_WR4Jhighx_bin3 strong1L_WR4Jlowx_bin1 strong1L_WR4Jlowx_bin2 strong1L_WR4Jlowx_bin3 strong1L_WR6J_bin1 strong1L_WR6J_bin2 strong1L_WR6J_bin3 strong1L_WR6J_bin4; do
    dirstr=$(echo $d | sed 's/_/\\_/g')
    COUNTER=0
    cat >> $1 <<EOF
\begin{frame}[fragile]
\frametitle{${dirstr}}
\section{${dirstr}}
\begin{changemargin}{-1cm}{-1cm}
\begin{columns}
EOF
    vars=()
    if [[ $d == *"strong"* ]]; then
      vars=(met met_Phi lep1Pt lep1Pt_soft lep1Eta jet1Eta meff met_over_meff ht jet1Pt jet2Pt mt njet nbjet30 aplanarity combined_mu ptmetlep)
    elif [[ $d == *"1Lbb"* ]]; then
      vars=(met lep1Pt lep1Eta jet1Eta meff met_over_meff ht jet1Pt jet2Pt jet3Pt mt mct mbb mjj dRJet dphimetlep njet nbjet30 mu ptmetlep)
    elif [[ $d == *"weak"* ]]; then
      vars=(met lep1Pt lep1Eta jet1Eta meff met_over_meff ht jet1Pt jet2Pt jet3Pt mt mct mjj dRJet dphimetlep njet nbjet30 mu ptmetlep)
    else
      echo "lol, stupid"
    fi

    for (( i=0; i<${#vars[@]} ; i+=2 )) ; do
      varstr1=$(echo ${vars[i]} | sed 's/_/\\_/g')
      varstr2=$(echo ${vars[i+1]} | sed 's/_/\\_/g')
      COUNTER=$[$COUNTER +1]


      cat >> $1 <<EOF
\column{0.33\linewidth}
\centering
\tiny
\includegraphics[width=\linewidth]{${input}/${d}/hists/${vars[i]}.pdf}
EOF

    if [ -z "$varstr2" ]; then
      echo "empty"
    else
      cat >> $1 <<EOF

\includegraphics[width=\linewidth]{${input}/${d}/hists/${vars[i+1]}.pdf}

EOF
    fi

        if (( $COUNTER == 3 )); then
            COUNTER=0
            cat >> $1 <<EOF
\end{columns}
\end{changemargin}
\end{frame}

\begin{frame}[fragile]
\frametitle{${dirstr}}
\begin{changemargin}{-1cm}{-1cm}
\begin{columns}
EOF
fi
done

cat >> $1 <<EOF
\end{columns}
\end{changemargin}
\end{frame}
EOF

done

cat >> $1 <<EOF
\end{document}
EOF
