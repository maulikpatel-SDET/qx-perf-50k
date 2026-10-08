"""Service module 33139: business logic, no crypto."""


def calculate_total_33139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33139():
    return 'module 33139 handles orders and invoices'
