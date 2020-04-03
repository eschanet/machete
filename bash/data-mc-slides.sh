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

for d in alt_strong-1L_presel alt_strong-1L_presel_BV alt_strong-1L_presel_BT alt_strong-1L_presel_electron alt_strong-1L_presel_muon alt_strong-1L_TR2J_bin1 alt_strong-1L_TR2J_bin2 alt_strong-1L_TR2J_bin3 alt_strong-1L_TR4J_bin1 alt_strong-1L_TR4J_bin2 alt_strong-1L_TR4J_bin3 alt_strong-1L_TR6J_bin1 alt_strong-1L_TR6J_bin2 alt_strong-1L_TR6J_bin3 alt_strong-1L_TR6J_bin4 alt_strong-1L_VR2JBT_bin1 alt_strong-1L_VR2JBT_bin2 alt_strong-1L_VR2JBT_bin3 alt_strong-1L_VR2JBV_bin1 alt_strong-1L_VR2JBV_bin2 alt_strong-1L_VR2JBV_bin3 alt_strong-1L_VR4JBT_bin1 alt_strong-1L_VR4JBT_bin2 alt_strong-1L_VR4JBT_bin3 alt_strong-1L_VR4JBV_bin1 alt_strong-1L_VR4JBV_bin2 alt_strong-1L_VR4JBV_bin3 alt_strong-1L_VR6JBT_bin1 alt_strong-1L_VR6JBT_bin2 alt_strong-1L_VR6JBT_bin3 alt_strong-1L_VR6JBV_bin1 alt_strong-1L_VR6JBV_bin2 alt_strong-1L_VR6JBV_bin3 alt_strong-1L_WR2J_bin1 alt_strong-1L_WR2J_bin2 alt_strong-1L_WR2J_bin3 alt_strong-1L_WR4J_bin1 alt_strong-1L_WR4J_bin2 alt_strong-1L_WR4J_bin3 alt_strong-1L_WR6J_bin1 alt_strong-1L_WR6J_bin2 alt_strong-1L_WR6J_bin3 alt_strong-1L_WR6J_bin4; do
    dirstr=$(echo $d | sed 's/_/\\_/g')
    COUNTER=0
    NEWDIR=1
    cat >> $1 <<EOF
\begin{frame}[fragile]
\frametitle{${dirstr}}
\section{${dirstr}}
\begin{changemargin}{-1cm}{-1cm}
\begin{columns}
EOF
    vars=()
    if [[ $d == *"strong"* ]]; then
      vars=(met met_Phi lep1Pt lep1Pt_soft lep1Eta jet1Eta mt ptmetlep dphimetlep ht meff met_over_meff jet1Pt jet2Pt njet nbjet30 aplanarity combined_mu )
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

      if [[ $COUNTER == 0 ]] && [[ $NEWDIR == 0 ]]; then
cat >> $1 <<EOF
\begin{frame}[fragile]
\frametitle{${dirstr}}
\begin{changemargin}{-1cm}{-1cm}
\begin{columns}
EOF
fi

      COUNTER=$[$COUNTER +1]
      NEWDIR=0

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
EOF
fi
done

done

cat >> $1 <<EOF
\end{document}
EOF
