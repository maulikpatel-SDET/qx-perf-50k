"""Service module 20790: business logic, no crypto."""


def calculate_total_20790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20790():
    return 'module 20790 handles orders and invoices'
