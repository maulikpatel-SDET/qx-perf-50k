"""Service module 29327: business logic, no crypto."""


def calculate_total_29327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29327():
    return 'module 29327 handles orders and invoices'
