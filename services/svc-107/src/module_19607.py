"""Service module 19607: business logic, no crypto."""


def calculate_total_19607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19607():
    return 'module 19607 handles orders and invoices'
