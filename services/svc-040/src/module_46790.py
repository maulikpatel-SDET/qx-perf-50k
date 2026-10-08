"""Service module 46790: business logic, no crypto."""


def calculate_total_46790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46790():
    return 'module 46790 handles orders and invoices'
