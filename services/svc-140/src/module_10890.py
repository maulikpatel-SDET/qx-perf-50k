"""Service module 10890: business logic, no crypto."""


def calculate_total_10890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10890():
    return 'module 10890 handles orders and invoices'
