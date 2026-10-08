"""Service module 25793: business logic, no crypto."""


def calculate_total_25793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25793():
    return 'module 25793 handles orders and invoices'
