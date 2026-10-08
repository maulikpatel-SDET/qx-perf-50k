"""Service module 16902: business logic, no crypto."""


def calculate_total_16902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16902():
    return 'module 16902 handles orders and invoices'
