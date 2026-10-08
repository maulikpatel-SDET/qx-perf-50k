"""Service module 44385: business logic, no crypto."""


def calculate_total_44385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44385():
    return 'module 44385 handles orders and invoices'
