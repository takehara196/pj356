# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd


def make_table():
    agents_cols = [
        "id",
        "email",
        "encrypted_password",
        "reset_password_token",
        "reset_password_sent_at",
        "remember_created_at",
        "confirmation_token",
        "confirmed_at",
        "confirmation_sent_at",
        "unconfirmed_email",
        "created_at",
        "updated_at",
        "nickname",
        "family_name",
        "first_name",
        "tel",
        "budget_min",
        "budget_max",
        "desired_area",
        "residense_type",
        "preference1",
        "preference2",
        "preference3",
        "preference4",
        "preference5",
        "preference6",
        "preference7",
        "preference8",
        "preference9",
        "needs_1",
        "needs_2",
        "needs_3",
        "needs_4",
        "needs_5",
        "needs_free_text",
        "avatar"
    ]

    buyers_cols = [
        "id",
        "email",
        "encrypted_password",
        "reset_password_token",
        "reset_password_sent_at",
        "remember_created_at",
        "confirmation_token",
        "confirmed_at",
        "confirmation_sent_at",
        "unconfirmed_email",
        "created_at",
        "updated_at",
        "nickname",
        "family_name",
        "first_name",
        "tel",
        "budget_min",
        "budget_max",
        "desired_area",
        "residense_type",
        "preference1",
        "preference2",
        "preference3",
        "preference4",
        "preference5",
        "preference6",
        "preference7",
        "preference8",
        "preference9",
        "needs_1",
        "needs_2",
        "needs_3",
        "needs_4",
        "needs_5",
        "needs_free_text",
        "avatar"
    ]

    # レコード数
    r = 1000
    agent_df = pd.DataFrame(
        index=range(r),
        columns=agents_cols
    )

    # preference1, ..., needs_5列にランダムの数値を付与する

    print(agent_df)

    return


def main():
    make_table()


if __name__ == '__main__':
    main()
