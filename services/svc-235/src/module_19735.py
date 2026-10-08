"""Service module 19735: business logic, no crypto."""


def calculate_total_19735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19735():
    return 'module 19735 handles orders and invoices'
