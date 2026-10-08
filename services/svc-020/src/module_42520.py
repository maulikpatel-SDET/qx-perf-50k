"""Service module 42520: business logic, no crypto."""


def calculate_total_42520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42520():
    return 'module 42520 handles orders and invoices'
