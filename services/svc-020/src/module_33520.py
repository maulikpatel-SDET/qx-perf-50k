"""Service module 33520: business logic, no crypto."""


def calculate_total_33520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33520():
    return 'module 33520 handles orders and invoices'
