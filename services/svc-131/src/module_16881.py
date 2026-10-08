"""Service module 16881: business logic, no crypto."""


def calculate_total_16881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16881():
    return 'module 16881 handles orders and invoices'
