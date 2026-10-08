"""Service module 16566: business logic, no crypto."""


def calculate_total_16566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16566():
    return 'module 16566 handles orders and invoices'
