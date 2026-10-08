"""Service module 20646: business logic, no crypto."""


def calculate_total_20646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20646():
    return 'module 20646 handles orders and invoices'
