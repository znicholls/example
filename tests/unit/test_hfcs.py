def test_hfc_impulse_response():
    time = np.array([0, 1, 2, 3])
    input_emissions = np.array([10, 0, 0, 0])
    expected = 10 * np.exp(-time)

    result = calculate_hfc_conc(input_emissions, lifetime=1.0)

    assert result == expected
    # assert np.testing.assert_allclose(result, expected)
