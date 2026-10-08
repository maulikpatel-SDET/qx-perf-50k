"""Service module 27186: business logic, no crypto."""


def calculate_total_27186(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27186():
    return 'module 27186 handles orders and invoices'
