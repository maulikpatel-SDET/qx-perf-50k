"""Service module 33935: business logic, no crypto."""


def calculate_total_33935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33935():
    return 'module 33935 handles orders and invoices'
