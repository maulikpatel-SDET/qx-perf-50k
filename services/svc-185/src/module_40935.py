"""Service module 40935: business logic, no crypto."""


def calculate_total_40935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40935():
    return 'module 40935 handles orders and invoices'
