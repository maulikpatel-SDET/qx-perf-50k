"""Service module 19328: business logic, no crypto."""


def calculate_total_19328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19328():
    return 'module 19328 handles orders and invoices'
