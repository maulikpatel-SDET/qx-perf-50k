"""Service module 17520: business logic, no crypto."""


def calculate_total_17520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17520():
    return 'module 17520 handles orders and invoices'
