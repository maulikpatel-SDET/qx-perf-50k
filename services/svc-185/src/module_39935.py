"""Service module 39935: business logic, no crypto."""


def calculate_total_39935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39935():
    return 'module 39935 handles orders and invoices'
