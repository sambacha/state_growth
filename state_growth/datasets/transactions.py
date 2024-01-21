from __future__ import annotations

import polars as pl


def aggregate_transactions(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.group_by('block_number')
        .agg(
            n_txs=pl.len(),
            n_from_addresses=pl.col.from_address.n_unique(),
            n_to_addresses=pl.col.to_address.n_unique(),
            gas_used=pl.sum('gas_used'),
            n_input_bytes=pl.sum('n_input_bytes'),
            n_input_zero_bytes=pl.sum('n_input_zero_bytes'),
            n_input_nonzero_bytes=pl.sum('n_input_nonzero_bytes'),
            n_rlp_bytes=pl.sum('n_rlp_bytes'),
        )
        .sort('block_number')
    )
