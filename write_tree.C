void write_tree() {
//   example of macro to create can ntuple reading data from an ascii file.
//   This macro is a variant of basic.C
//Author: Rene Brun
   cout<<  "mark 1"<< endl;
   TString dir = gSystem->UnixPathName(__FILE__);
   dir.ReplaceAll("write_tree.C","");
   dir.ReplaceAll("/./","/");


   TFile *f = new TFile("test.root","RECREATE");
   //TH1F *h1 = new TH1F(,"x distribution",100,-4,4);

   TTree *T = new TTree("ntuple","data from primary file");


  Long64_t nlines = T->ReadFile(Form("%s000703-test.pri", dir.Data()),"prm_Crk_id:prm_energy:prm_x0:prm_theta:prm_phi:ph_obs_lev:el_obs_lev:hd_obs_lev:mu_obs_lev:tot_obs_lev") ;
  printf("found %11d points \n", nlines);
  //T->Draw(,"z>2")
  T->Write();


}
