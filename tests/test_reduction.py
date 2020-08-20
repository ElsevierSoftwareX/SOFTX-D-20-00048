import unittest
import numpy as np
from PCAfold import preprocess
from PCAfold import reduction
from PCAfold import PCA
from PCAfold import DataSampler


class TestReduction(unittest.TestCase):

    def test_PCA_allowed_initializations(self):

        test_data_set = np.random.rand(100,20)
        test_data_set_constant = np.random.rand(100,20)
        test_data_set_constant[:,10] = np.ones((100,))
        test_data_set_constant[:,5] = np.ones((100,))

        try:
            pca = PCA(test_data_set, scaling='auto')
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='auto')
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='std')
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='none')
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='auto', neta=2)
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='auto', neta=3, nocenter=True)
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='pareto', neta=2, nocenter=True)
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='auto', neta=2, useXTXeig=False)
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(test_data_set, scaling='range', neta=2, useXTXeig=False, nocenter=True)
        except Exception:
            self.assertTrue(False)

        try:
            (X_removed, idx_removed, idx_retained) = preprocess.remove_constant_vars(test_data_set_constant)
        except Exception:
            self.assertTrue(False)

        try:
            pca = PCA(X_removed, scaling='range', neta=2)
        except Exception:
            self.assertTrue(False)

    def test_PCA_not_allowed_initializations(self):

        test_data_set = np.random.rand(100,20)
        test_data_set_constant = np.random.rand(100,20)
        test_data_set_constant[:,10] = np.ones((100,))
        test_data_set_constant[:,5] = np.ones((100,))

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='none', neta=-1)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='auto', neta=30)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='auto', neta=3, useXTXeig=1)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='auto', nocenter=1)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling=False)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='none', neta=True)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='none', neta=5, nocenter='False')

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set, scaling='auto', neta=3, useXTXeig='True')

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set_constant, scaling='auto', neta=2)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set_constant)

        with self.assertRaises(ValueError):
            pca = PCA(test_data_set_constant, scaling='range', neta=5)

    def test_x2eta_allowed_calls(self):

        test_data_set = np.random.rand(10,2)

        pca = PCA(test_data_set, scaling='auto')

        try:
            pca.x2eta(test_data_set)
        except Exception:
            self.assertTrue(False)

        try:
            scores = pca.x2eta(test_data_set)
        except Exception:
            self.assertTrue(False)

        try:
            x = pca.eta2x(scores)
        except Exception:
            self.assertTrue(False)

        self.assertTrue(test_data_set.all() == x.all())

    def test_x2eta_not_allowed_calls(self):

        test_data_set = np.random.rand(10,2)
        test_data_set_2 = np.random.rand(10,3)

        pca = PCA(test_data_set, scaling='auto')

        with self.assertRaises(AssertionError):
            pca.x2eta(test_data_set_2)

    def test_pca_on_sampled_data_set_allowed_calls(self):

        X = np.random.rand(200,20)
        idx_X_r = np.arange(91,151,1)

        try:
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 2, 1, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 2, 2, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 2, 3, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 2, 4, X_source=[])
        except Exception:
            self.assertTrue(False)

        try:
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'range', 2, 1, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'range', 2, 2, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'range', 2, 3, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'range', 2, 4, X_source=[])
        except Exception:
            self.assertTrue(False)

        try:
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 1, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 2, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 3, X_source=[])
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 4, X_source=[])
        except Exception:
            self.assertTrue(False)

        X_source = np.random.rand(200,20)
        try:
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 1, X_source=X_source)
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 2, X_source=X_source)
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 3, X_source=X_source)
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 1, 4, X_source=X_source)
        except Exception:
            self.assertTrue(False)

        try:
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'pareto', 10, 1, X_source=X_source)
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'pareto', 10, 2, X_source=X_source)
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'pareto', 10, 3, X_source=X_source)
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'pareto', 10, 4, X_source=X_source)
        except Exception:
            self.assertTrue(False)

    def test_pca_on_sampled_data_set_not_allowed_calls(self):

        X = np.random.rand(200,20)
        idx_X_r = np.arange(91,151,1)

        with self.assertRaises(ValueError):
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 2, 5, X_source=[])

        with self.assertRaises(ValueError):
            (eigenvalues, eigenvectors, pc_scores, pc_sources, C, D, C_r, D_r) = reduction.pca_on_sampled_data_set(X, idx_X_r, 'auto', 2, 25, X_source=[])

    def test_equilibrate_cluster_populations_allowed_calls(self):

        X = np.random.rand(200,20)
        idx = np.zeros((200,))
        idx[20:60,] = 1
        idx[150:190] = 2

        try:
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 1, X_source=[], n_iterations=10, stop_iter=0, random_seed=None, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 2, X_source=[], n_iterations=10, stop_iter=0, random_seed=None, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 3, X_source=[], n_iterations=10, stop_iter=0, random_seed=None, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 4, X_source=[], n_iterations=10, stop_iter=0, random_seed=None, verbose=False)
        except Exception:
            self.assertTrue(False)

        try:
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 1, X_source=[], n_iterations=1, stop_iter=0, random_seed=None, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 2, X_source=[], n_iterations=1, stop_iter=0, random_seed=None, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 3, X_source=[], n_iterations=1, stop_iter=0, random_seed=None, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 2, 4, X_source=[], n_iterations=1, stop_iter=0, random_seed=None, verbose=False)
        except Exception:
            self.assertTrue(False)

        try:
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'range', 2, 1, X_source=[], n_iterations=1, stop_iter=0, random_seed=100, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'range', 2, 2, X_source=[], n_iterations=1, stop_iter=0, random_seed=100, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'range', 2, 3, X_source=[], n_iterations=1, stop_iter=0, random_seed=100, verbose=False)
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'range', 2, 4, X_source=[], n_iterations=1, stop_iter=0, random_seed=100, verbose=False)
        except Exception:
            self.assertTrue(False)

        X_source = np.random.rand(200,20)

    def test_analyze_eigenvector_weights_movement_allowed_calls(self):

        X = np.random.rand(200,20)
        idx = np.zeros((200,))
        idx[20:60,] = 1
        idx[150:190] = 2

        try:
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 20, 1, X_source=[], n_iterations=20, stop_iter=0, random_seed=None, verbose=False)
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,0,:], variable_names=[], plot_variables=[], normalize=False, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,0,:], variable_names=[], plot_variables=[2,5,10], normalize=False, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,1,:], variable_names=[], plot_variables=[2,5,10], normalize=False, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,0,:], variable_names=[], plot_variables=[2,5,10], normalize=True, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,1,:], variable_names=[], plot_variables=[2,5,10], normalize=True, zero_norm=True, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,15,:], variable_names=[], plot_variables=[2,5,10], normalize=True, zero_norm=True, legend_label=[], title=None, save_filename=None)
            plt.close()
        except Exception:
            self.assertTrue(False)

        try:
            (eigenvalues, eigenvectors_matrix, pc_scores_matrix, pc_sources_matrix, idx_train, C_r, D_r) = reduction.equilibrate_cluster_populations(X, idx, 'auto', 20, 1, X_source=[], n_iterations=2, stop_iter=0, random_seed=None, verbose=False)
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,0,:], variable_names=[], plot_variables=[], normalize=False, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,0,:], variable_names=[], plot_variables=[2,5,10], normalize=False, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,1,:], variable_names=[], plot_variables=[2,5,10], normalize=False, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,1,:], variable_names=[], plot_variables=[2,5,10], normalize=True, zero_norm=False, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,1,:], variable_names=[], plot_variables=[2,5,10], normalize=True, zero_norm=True, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvector_weights_movement(eigenvectors_matrix[:,15,:], variable_names=[], plot_variables=[2,5,10], normalize=True, zero_norm=True, legend_label=[], title=None, save_filename=None)
            plt.close()
        except Exception:
            self.assertTrue(False)

    def test_analyze_eigenvalue_distribution_allowed_calls(self):

        X = np.random.rand(200,20)
        idx_X_r = np.arange(91,151,1)

        try:
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'auto', 1, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'auto', 2, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'auto', 3, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'auto', 4, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'pareto', 1, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'pareto', 2, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'pareto', 3, legend_label=[], title=None, save_filename=None)
            plt.close()
            plt = reduction.analyze_eigenvalue_distribution(X, idx_X_r, 'pareto', 4, legend_label=[], title=None, save_filename=None)
            plt.close()
        except Exception:
            self.assertTrue(False)
